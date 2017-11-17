#include "analysis1.h"
#include "ui_analysis1.h"

analysis1::analysis1(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::analysis1)
{
    ui->setupUi(this);

    QPixmap bg2("C:/Users/HP/fifa2017analysis/background2.jpg");
    ui->background2->setPixmap(bg2);
    QPixmap graph1("C:/Users/HP/fifa2017analysis/complete-fifa-2017-player-dataset-global/Solution/Graph 1.png");
    ui->firstGraph->setPixmap(graph1);
    QPixmap rank1("C:/Users/HP/fifa2017analysis/complete-fifa-2017-player-dataset-global/Solution/Rank 1.png");
    ui->firstPlayer->setPixmap(rank1);
    QPixmap graph2("C:/Users/HP/fifa2017analysis/complete-fifa-2017-player-dataset-global/Solution/Graph 2.png");
    ui->secondGraph->setPixmap(graph2);
    QPixmap rank2("C:/Users/HP/fifa2017analysis/complete-fifa-2017-player-dataset-global/Solution/Rank 2.png");
    ui->secondPlayer->setPixmap(rank2);
    QPixmap graph3("C:/Users/HP/fifa2017analysis/complete-fifa-2017-player-dataset-global/Solution/Graph 3.png");
    ui->thirdGraph->setPixmap(graph3);
    QPixmap rank3("C:/Users/HP/fifa2017analysis/complete-fifa-2017-player-dataset-global/Solution/Rank 3.png");
    ui->thirdPlayer->setPixmap(rank3);

}

analysis1::~analysis1()
{
    delete ui;
}
