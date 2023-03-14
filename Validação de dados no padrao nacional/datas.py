from datetime import datetime, timedelta

class Datas:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        meses_do_ano =[
            "Janeiro", "Fervereiro", "Março",
            "Abril", "Maio", "Junho", "Julho"
            "Agosto", "Setembro", "Outubro"
            "Novembro", "Dezembro"
        ]
        mes_cadastro = self.momento_cadastro.month
        return meses_do_ano[mes_cadastro-1]

    def dia_semana(self):
        dia_semana_lista = [
            "Segunda", "Terça", "Quarta"
            "Quinta", "Sexta", "Sabado", "Domingo"
        ]
        dia_semana = self.momento_cadastro.weekday()
        return dia_semana_lista[dia_semana]

    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days=30)) - self.momento_cadastro
        return tempo_cadastro
