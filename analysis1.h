#ifndef ANALYSIS1_H
#define ANALYSIS1_H

#include <QMainWindow>

namespace Ui {
class analysis1;
}

class analysis1 : public QMainWindow
{
    Q_OBJECT

public:
    explicit analysis1(QWidget *parent = 0);
    ~analysis1();

private:
    Ui::analysis1 *ui;
};

#endif // ANALYSIS1_H
