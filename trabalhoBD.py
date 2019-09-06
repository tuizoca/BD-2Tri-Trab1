#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql
import pymysql.cursors

con = pymysql.connect(host='192.168.56.101',
                      user='admin',
                      password='admin123',
                      db='python',
                      charset='utf8',
                      cursorclass=pymysql.cursors.DictCursor)



with con:

    cur = con.cursor()

    while true:
        println("Lista de tarefas MASTER POWER 2.0")
        println("MENU")
        println("1-Incluir tarefa")
        println("2-Concluir tarefa")
        println("3-Remover tarefa")
        println("4-Mostrar tarefas")
        println("5-Sair")
        println("6-Bazinga")
        opc = input()
        if opc == 5:
            break

        elif opc == 1:
            println("Descricao:")
            descricao = input()
            println("Prioridade de 1-5")
            prioridade = input()
            println("Data limite")
            data = input()
            cur.execute("INSERT INTO listaTarefas.tarefas(descricao,prioridade,data,status) VALUES(%s, %s, %s,false)", (descricao, prioridade, data))

        elif opc == 2:
            println("ID da atividade")
            Idn = input()
            cur.execute("SELECT * FROM tarefas WHERE id = 'Idn'")
            cur.execute("UPDATE tarefas SET status = false ")

        elif opc == 3:
            println("ID da atividade")
            Idn = input()
            cur.execute("SELECT * FROM tarefas WHERE id = Idn")
            cur.execute("DELETE FROM tarefas WHERE id = Idn")      

        elif opc == 4:
            cur.execute("SELECT * FROM tarefas")
            rows = cur.fetchall()
            for row in rows:
                print(row["id"], row["descricao"], row["prioridade"], row["data"], row["status"])
