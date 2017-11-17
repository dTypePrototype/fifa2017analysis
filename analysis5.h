#ifndef ANALYSIS5_H
#define ANALYSIS5_H

#include <QDialog>

namespace Ui {
class analysis5;
}

class analysis5 : public QDialog
{
    Q_OBJECT

public:
    explicit analysis5(QWidget *parent = 0);
    ~analysis5();

private:
    Ui::analysis5 *ui;
};

#endif // ANALYSIS5_H
