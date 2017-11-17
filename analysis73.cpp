#include "analysis73.h"
#include "ui_analysis73.h"

analysis73::analysis73(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::analysis73)
{
    ui->setupUi(this);
    QPixmap bg("C:/Users/HP/fifa2017analysis/background8.jpg");
    ui->background->setPixmap(bg);
    QPixmap gph1("C:/Users/HP/fifa2017analysis/complete-fifa-2017-player-dataset-global/Solution/at1.png");
    ui->graph_1->setPixmap(gph1);
    QPixmap gph2("C:/Users/HP/fifa2017analysis/complete-fifa-2017-player-dataset-global/Solution/at2.png");
    ui->graph_2->setPixmap(gph2);
    QPixmap gph3("C:/Users/HP/fifa2017analysis/complete-fifa-2017-player-dataset-global/Solution/at3.png");
    ui->graph_3->setPixmap(gph3);
}

analysis73::~analysis73()
{
    delete ui;
}
