#include "mainwindow.h"
#include "ui_mainwindow.h"
#include<QFileDialog>
#include<QMessageBox>
#include<QDesktopServices>
#include<QUrl>
#include "analysis1.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    QPixmap pix("C:/Users/HP/fifa2017analysis/backgroundImage.jpg");
    ui->backgroundImage->setPixmap(pix);
    QPixmap fifaLogo("C:/Users/HP/fifa2017analysis/mainHeading.png");
    ui->mainHeading->setPixmap(fifaLogo);
    QPixmap ealogo("C:/Users/HP/fifa2017analysis/EALogo.png");
    ui->eaLogo->setPixmap(ealogo);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_codeButton_clicked()
{
    QDesktopServices::openUrl(QUrl("C:/Users/HP/fifa2017analysis/bestTeam.txt",QUrl::TolerantMode));
}

void MainWindow::on_datasetButton_clicked()
{
    QDesktopServices::openUrl(QUrl("C:/Users/HP/fifa2017analysis/complete-fifa-2017-player-dataset-global",QUrl::TolerantMode));
}

void MainWindow::on_anysis1_clicked()
{
    newwindow =new analysis1();
    newwindow->show();
}
