#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    QPixmap pix("C:/Users/HP/fifa2017analysis/backgroundImage.jpg");
    ui->backgroundImage->setPixmap(pix);
    QPixmap fifaLogo("C:/Users/HP/fifa2017analysis/fifaLogo.png");
    ui->mainHeading->setPixmap(fifaLogo);
    QPixmap ealogo("C:/Users/HP/fifa2017analysis/EALogo.png");
    ui->eaLogo->setPixmap(ealogo);


}

MainWindow::~MainWindow()
{
    delete ui;
}
