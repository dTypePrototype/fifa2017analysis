#include "analysis1.h"
#include "ui_analysis1.h"

analysis1::analysis1(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::analysis1)
{
    ui->setupUi(this);
}

analysis1::~analysis1()
{
    delete ui;
}
