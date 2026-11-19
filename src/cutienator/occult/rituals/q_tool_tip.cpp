//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qtooltip.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtooltip.h>
#include <QtCore/qpoint.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtGui/qpalette.h>
#include <QtGui/qfont.h>

//  void QToolTip::showText(const QPoint &pos, const QString &text, QWidget
//      *w, const QRect &rect, int msecShowTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QToolTip8showTextERK6QPointRK7QStringP7QWidgetRK5QRecti(
    const QPoint *pos,
    const QString *text,
    QWidget *w,
    const QRect *rect,
    int msecShowTime) {
  QToolTip::showText(*pos, *text, w, *rect, msecShowTime);
}

//  void QToolTip::hideText()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QToolTip8hideTextEv() {
  QToolTip::hideText();
}

//  bool QToolTip::isVisible()
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QToolTip9isVisibleEv() {
  return QToolTip::isVisible();
}

//  QString QToolTip::text()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8QToolTip4textEv() {
  return new QString(QToolTip::text());
}

//  QPalette QToolTip::palette()
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZN8QToolTip7paletteEv() {
  return new QPalette(QToolTip::palette());
}

//  void QToolTip::setPalette(const QPalette &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QToolTip10setPaletteERK8QPalette(const QPalette *a0) {
  QToolTip::setPalette(*a0);
}

//  QFont QToolTip::font()
extern "C" Q_DECL_EXPORT
QFont *ritual_ZN8QToolTip4fontEv() {
  return new QFont(QToolTip::font());
}

//  void QToolTip::setFont(const QFont &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QToolTip7setFontERK5QFont(const QFont *a0) {
  QToolTip::setFont(*a0);
}

//  QToolTip::~QToolTip()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QToolTipD1Ev(QToolTip *self) {
  delete self;
}
