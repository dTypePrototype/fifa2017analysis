#ifndef MAINWINDOW_H
#define MAINWINDOW_H


#include <QMainWindow>
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

    void on_anysis1_clicked();

    void on_anysis2_clicked();

    void on_anysis3_clicked();

    void on_anysis4_clicked();

    void on_anysis5_clicked();

    void on_anysis6_clicked();

    void on_anysis7_clicked();

    void on_exitButton_clicked();

private:
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
