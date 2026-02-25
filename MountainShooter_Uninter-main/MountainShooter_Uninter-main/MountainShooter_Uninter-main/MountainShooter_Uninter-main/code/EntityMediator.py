#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.Player import Player
from code.PlayerShot import PlayerShot

class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        """Verifica se as entidades saíram dos limites da tela para removê-las"""
        if isinstance(ent, Enemy):
            # Se o inimigo (incluindo Enemy3) ultrapassar a borda esquerda, morre
            if ent.rect.right <= 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            # Se o tiro do jogador ultrapassar a borda direita, é removido
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            # Se o tiro do inimigo ultrapassar a borda esquerda, é removido
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        """Verifica colisões entre duas entidades (Ex: Tiro vs Inimigo)"""
        valid_interaction = False
        # Filtra apenas interações válidas para evitar que inimigos batam em inimigos
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            valid_interaction = True
        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            valid_interaction = True

        if valid_interaction:
            # Lógica de colisão por sobreposição de Retângulos (AABB)
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):
                # Aplica o dano definido no Const.py em ambas as entidades
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                # Registra quem causou o dano para atribuição de Score posterior
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        """Atribui os pontos do inimigo morto ao jogador que deu o último tiro"""
        if enemy.last_dmg == 'Player1Shot':
            for ent in entity_list:
                if ent.name == 'Player1':
                    ent.score += enemy.score # Soma pontos do inimigo (Ex: 250 do Enemy3)
        elif enemy.last_dmg == 'Player2Shot':
            for ent in entity_list:
                if ent.name == 'Player2':
                    ent.score += enemy.score

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        """Gerenciador principal que percorre a lista de entidades para checar colisões"""
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            # Checa colisão com as bordas da janela
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                # Checa colisão entre as entidades da lista
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        """Remove entidades com vida zero e aciona o sistema de score para inimigos"""
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    # Antes de remover o inimigo, dá a pontuação ao Player
                    EntityMediator.__give_score(ent, entity_list)
                entity_list.remove(ent)