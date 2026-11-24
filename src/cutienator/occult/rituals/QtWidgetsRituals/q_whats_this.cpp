//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qwhatsthis.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(whatsthis)
#if QT_CONFIG(whatsthis)
#include <QtWidgets/qwhatsthis.h>
#include <QtCore/qpoint.h>
#include <QtCore/qstring.h>

//  void QWhatsThis::enterWhatsThisMode()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QWhatsThis18enterWhatsThisModeEv() {
  QWhatsThis::enterWhatsThisMode();
}

//  bool QWhatsThis::inWhatsThisMode()
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QWhatsThis15inWhatsThisModeEv() {
  return QWhatsThis::inWhatsThisMode();
}

//  void QWhatsThis::leaveWhatsThisMode()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QWhatsThis18leaveWhatsThisModeEv() {
  QWhatsThis::leaveWhatsThisMode();
}

//  void QWhatsThis::showText(const QPoint &pos, const QString &text, QWidget
//      *w)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QWhatsThis8showTextERK6QPointRK7QStringP7QWidget(
    const QPoint *pos,
    const QString *text,
    QWidget *w) {
  QWhatsThis::showText(*pos, *text, w);
}

//  void QWhatsThis::hideText()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QWhatsThis8hideTextEv() {
  QWhatsThis::hideText();
}

#if QT_CONFIG(action)
//  QAction *QWhatsThis::createAction(QObject *parent)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN10QWhatsThis12createActionEP7QObject(QObject *parent) {
  return QWhatsThis::createAction(parent);
}
#endif  // QT_CONFIG(action)

//  QWhatsThis::~QWhatsThis()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QWhatsThisD1Ev(QWhatsThis *self) {
  delete self;
}

#endif  // QT_CONFIG(whatsthis)
#endif  // QT_CONFIG(whatsthis)
