#include "analysis72.h"
#include "ui_analysis72.h"
#include "analysis73.h"

analysis72::analysis72(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::analysis72)
{
    ui->setupUi(this);
    QPixmap bg("C:/Users/HP/fifa2017analysis/background8.jpg");
    ui->background->setPixmap(bg);
    QPixmap gph1("C:/Users/HP/fifa2017analysis/complete-fifa-2017-player-dataset-global/Solution/mf1.png");
    ui->graph1->setPixmap(gph1);
    QPixmap gph2("C:/Users/HP/fifa2017analysis/complete-fifa-2017-player-dataset-global/Solution/mf2.png");
    ui->graph2->setPixmap(gph2);
    QPixmap gph3("C:/Users/HP/fifa2017analysis/complete-fifa-2017-player-dataset-global/Solution/mf3.png");
    ui->graph3->setPixmap(gph3);
    QPixmap gph4("C:/Users/HP/fifa2017analysis/complete-fifa-2017-player-dataset-global/Solution/mf4.png");
    ui->graph4->setPixmap(gph4);
}

analysis72::~analysis72()
{
    delete ui;
}

void analysis72::on_nextButton_clicked()
{
    analysis73 obj;
    obj.setModal(true);
    obj.exec();
}
