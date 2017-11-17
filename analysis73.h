#ifndef ANALYSIS73_H
#define ANALYSIS73_H

#include <QDialog>

namespace Ui {
class analysis73;
}

class analysis73 : public QDialog
{
    Q_OBJECT

public:
    explicit analysis73(QWidget *parent = 0);
    ~analysis73();

private:
    Ui::analysis73 *ui;
};

#endif // ANALYSIS73_H
