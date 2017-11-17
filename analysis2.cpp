#include "analysis2.h"
#include "ui_analysis2.h"

analysis2::analysis2(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::analysis2)
{
    ui->setupUi(this);
    QPixmap bg3("C:/Users/HP/fifa2017analysis/background3.jpg");
    ui->background3->setPixmap(bg3);
    QPixmap mn("C:/Users/HP/fifa2017analysis/complete-fifa-2017-player-dataset-global/Solution/Mean.png");
    ui->mean->setPixmap(mn);
    QPixmap mdn("C:/Users/HP/fifa2017analysis/complete-fifa-2017-player-dataset-global/Solution/Median.png");
    ui->median->setPixmap(mdn);
    QPixmap mod("C:/Users/HP/fifa2017analysis/complete-fifa-2017-player-dataset-global/Solution/Mode.png");
    ui->mode->setPixmap(mod);
    QPixmap stdDev("C:/Users/HP/fifa2017analysis/complete-fifa-2017-player-dataset-global/Solution/SD.png");
    ui->standardDeviation->setPixmap(stdDev);
}

analysis2::~analysis2()
{
    delete ui;
}
