#ifndef ANALYSIS4_H
#define ANALYSIS4_H

#include <QDialog>

namespace Ui {
class analysis4;
}

class analysis4 : public QDialog
{
    Q_OBJECT

public:
    explicit analysis4(QWidget *parent = 0);
    ~analysis4();

private:
    Ui::analysis4 *ui;
};

#endif // ANALYSIS4_H
