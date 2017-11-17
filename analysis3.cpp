#include "analysis3.h"
#include "ui_analysis3.h"

analysis3::analysis3(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::analysis3)
{
    ui->setupUi(this);
    QPixmap bg("C:/Users/HP/fifa2017analysis/background4.jpg");
    ui->background->setPixmap(bg);
}

analysis3::~analysis3()
{
    delete ui;
}
