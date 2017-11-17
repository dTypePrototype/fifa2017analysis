#include "analysis6.h"
#include "ui_analysis6.h"

analysis6::analysis6(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::analysis6)
{
    ui->setupUi(this);
    QPixmap bg("C:/Users/HP/fifa2017analysis/background7.jpg");
    ui->background->setPixmap(bg);
    QPixmap graph("C:/Users/HP/fifa2017analysis/complete-fifa-2017-player-dataset-global/Solution/best_goalkeeper.png");
    ui->goalkeeper_graph->setPixmap(graph);
}

analysis6::~analysis6()
{
    delete ui;
}
