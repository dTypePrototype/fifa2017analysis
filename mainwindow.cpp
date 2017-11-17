#include "mainwindow.h"
#include "ui_mainwindow.h"
#include<QFileDialog>
#include<QMessageBox>
#include<QDesktopServices>
#include<QUrl>
#include <QMediaPlayer>
#include <QVideoWidget>
#include "analysis1.h"
#include "analysis2.h"
#include "analysis3.h"
#include "analysis4.h"
#include "analysis5.h"
#include "analysis6.h"
#include "analysis7.h"
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
    QDesktopServices::openUrl(QUrl("C:/Users/HP/fifa2017analysis/complete-fifa-2017-player-dataset-global/Solution",QUrl::TolerantMode));
}

void MainWindow::on_datasetButton_clicked()
{
    QDesktopServices::openUrl(QUrl("C:/Users/HP/fifa2017analysis/complete-fifa-2017-player-dataset-global",QUrl::TolerantMode));
}

void MainWindow::on_anysis1_clicked()
{
    analysis1 obj;
    obj.setModal(true);
    obj.exec();
}

void MainWindow::on_anysis2_clicked()
{
    analysis2 obj;
    obj.setModal(true);
    obj.exec();
}

void MainWindow::on_anysis3_clicked()
{
    analysis3 obj;
    obj.setModal(true);
    obj.exec();
}

void MainWindow::on_anysis4_clicked()
{
    analysis4 obj;
    obj.setModal(true);
    obj.exec();
}

void MainWindow::on_anysis5_clicked()
{
    analysis5 obj;
    obj.setModal(true);
    obj.exec();
}

void MainWindow::on_anysis6_clicked()
{
    analysis6 obj;
    obj.setModal(true);
    obj.exec();
}



void MainWindow::on_anysis7_clicked()
{
    analysis7 obj;
    obj.setModal(true);
    obj.exec();
}

void MainWindow::on_exitButton_clicked()
{
    QMediaPlayer* player =new QMediaPlayer;
    QVideoWidget*vw =new QVideoWidget;
    player->setVideoOutput(vw);
    player->setMedia(QUrl::fromLocalFile("C:/Users/HP/fifa2017analysis/credits.avi"));
    vw->setGeometry(0,0,1920,1028);
    vw->showFullScreen();
    player->play();
    close();
}
