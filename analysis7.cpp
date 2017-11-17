#include "analysis7.h"
#include "ui_analysis7.h"
#include "analysis71.h"

analysis7::analysis7(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::analysis7)
{
    ui->setupUi(this);
    QPixmap bg("C:/Users/HP/fifa2017analysis/background8.jpg");
    ui->background->setPixmap(bg);
    QPixmap gph("C:/Users/HP/fifa2017analysis/complete-fifa-2017-player-dataset-global/Solution/best_goalkeeper.png");
    ui->graph->setPixmap(gph);
}

analysis7::~analysis7()
{
    delete ui;
}

void analysis7::on_nextButton_clicked()
{
    analysis71 obj;
    obj.setModal(true);
    obj.exec();
}
