#include "mainwindow.h"
#include <QApplication>
#include <QMediaPlayer>
#include <QVideoWidget>
#include <QThread>

class Sleeper : public QThread
{
public:
    static void sleep(unsigned long secs){QThread::sleep(secs);}
};
int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    QMediaPlayer* player =new QMediaPlayer;
    QVideoWidget*vw =new QVideoWidget;
    player->setVideoOutput(vw);
    player->setMedia(QUrl::fromLocalFile("C:/Users/HP/fifa2017analysis/introVideo.mov"));
    vw->setGeometry(0,0,1920,1028);
    MainWindow w;
    vw->showFullScreen();
    player->play();
    Sleeper::sleep(12);
    vw->close();
    w.showFullScreen();
    return a.exec();
}
