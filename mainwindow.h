#ifndef MAINWINDOW_H
#define MAINWINDOW_H


#include <QMainWindow>
#include"analysis1.h"
namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();



private slots:
    void on_codeButton_clicked();

    void on_datasetButton_clicked();

    void on_analysis1_clicked();

    void on_anysis1_clicked();

private:
    Ui::MainWindow *ui;
    analysis1 *newwindow;
};

#endif // MAINWINDOW_H
