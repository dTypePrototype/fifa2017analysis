#include "analysis71.h"
#include "ui_analysis71.h"
#include "analysis72.h"
analysis71::analysis71(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::analysis71)
{
    ui->setupUi(this);
    QPixmap bg("C:/Users/HP/fifa2017analysis/background8.jpg");
    ui->background->setPixmap(bg);
    ui->background->setPixmap(bg);
    QPixmap gph1("C:/Users/HP/fifa2017analysis/complete-fifa-2017-player-dataset-global/Solution/def1.png");
    ui->graph1->setPixmap(gph1);
    QPixmap gph2("C:/Users/HP/fifa2017analysis/complete-fifa-2017-player-dataset-global/Solution/df_2.png");
    ui->graph2->setPixmap(gph2);
    QPixmap gph3("C:/Users/HP/fifa2017analysis/complete-fifa-2017-player-dataset-global/Solution/df_3.png");
    ui->graph3->setPixmap(gph3);
    QPixmap gph4("C:/Users/HP/fifa2017analysis/complete-fifa-2017-player-dataset-global/Solution/df_4.png");
    ui->graph4->setPixmap(gph4);
}

analysis71::~analysis71()
{
    delete ui;
}

void analysis71::on_nextButton_clicked()
{
    analysis72 obj;
    obj.setModal(true);
    obj.exec();
}
