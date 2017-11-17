#ifndef ANALYSIS7_H
#define ANALYSIS7_H

#include <QDialog>

namespace Ui {
class analysis7;
}

class analysis7 : public QDialog
{
    Q_OBJECT

public:
    explicit analysis7(QWidget *parent = 0);
    ~analysis7();

private slots:
    void on_nextButton_clicked();

private:
    Ui::analysis7 *ui;
};

#endif // ANALYSIS7_H
