#ifndef ANALYSIS2_H
#define ANALYSIS2_H

#include <QDialog>

namespace Ui {
class analysis2;
}

class analysis2 : public QDialog
{
    Q_OBJECT

public:
    explicit analysis2(QWidget *parent = 0);
    ~analysis2();

private:
    Ui::analysis2 *ui;
};

#endif // ANALYSIS2_H
