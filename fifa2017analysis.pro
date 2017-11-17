#-------------------------------------------------
#
# Project created by QtCreator 2017-11-06T11:51:34
#
#-------------------------------------------------

QT       += core gui multimedia multimediawidgets

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = fifa2017analysis
TEMPLATE = app

# The following define makes your compiler emit warnings if you use
# any feature of Qt which as been marked as deprecated (the exact warnings
# depend on your compiler). Please consult the documentation of the
# deprecated API in order to know how to port your code away from it.
DEFINES += QT_DEPRECATED_WARNINGS

# You can also make your code fail to compile if you use deprecated APIs.
# In order to do so, uncomment the following line.
# You can also select to disable deprecated APIs only up to a certain version of Qt.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0


SOURCES += main.cpp\
        mainwindow.cpp \
    analysis1.cpp \
    analysis2.cpp \
    analysis3.cpp \
    analysis4.cpp \
    analysis5.cpp \
    analysis6.cpp \
    analysis7.cpp \
    analysis71.cpp \
    analysis72.cpp \
    analysis73.cpp

HEADERS  += mainwindow.h \
    analysis1.h \
    analysis2.h \
    analysis3.h \
    analysis4.h \
    analysis5.h \
    analysis6.h \
    analysis7.h \
    analysis71.h \
    analysis72.h \
    analysis73.h

FORMS    += mainwindow.ui \
    analysis1.ui \
    analysis2.ui \
    analysis3.ui \
    analysis4.ui \
    analysis5.ui \
    analysis6.ui \
    analysis7.ui \
    analysis71.ui \
    analysis72.ui \
    analysis73.ui

DISTFILES += \


RESOURCES += \
    resources.qrc
