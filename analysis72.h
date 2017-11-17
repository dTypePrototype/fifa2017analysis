#ifndef ANALYSIS72_H
#define ANALYSIS72_H

#include <QDialog>

namespace Ui {
class analysis72;
}

class analysis72 : public QDialog
{
    Q_OBJECT

public:
    explicit analysis72(QWidget *parent = 0);
    ~analysis72();

private slots:
    void on_nextButton_clicked();

private:
    Ui::analysis72 *ui;
};

#endif // ANALYSIS72_H
