#include "analysis5.h"
#include "ui_analysis5.h"

analysis5::analysis5(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::analysis5)
{
    ui->setupUi(this);
    QPixmap bg("C:/Users/HP/fifa2017analysis/background6.jpg");
    ui->background->setPixmap(bg);
    QPixmap barGph("C:/Users/HP/fifa2017analysis/complete-fifa-2017-player-dataset-global/Solution/contract_bar_graph.png");
    ui->bargraph->setPixmap(barGph);
    QPixmap piech("C:/Users/HP/fifa2017analysis/complete-fifa-2017-player-dataset-global/Solution/contract_pie_chart.png");
    ui->piechart->setPixmap(piech);


}

analysis5::~analysis5()
{
    delete ui;
}
