#include "analysis4.h"
#include "ui_analysis4.h"

analysis4::analysis4(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::analysis4)
{
    ui->setupUi(this);
    QPixmap bg("C:/Users/HP/fifa2017analysis/background5.jpg");
    ui->background->setPixmap(bg);
    QPixmap gph1("C:/Users/HP/fifa2017analysis/complete-fifa-2017-player-dataset-global/Solution/ana4.png");
    ui->graph1->setPixmap(gph1);
}

analysis4::~analysis4()
{
    delete ui;
}
