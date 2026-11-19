//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qsplashscreen.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qsplashscreen.h>
#include <QtCore/qstring.h>
#include <QtGui/qpixmap.h>
#include <QtGui/qcolor.h>

//  const QMetaObject *QSplashScreen::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QSplashScreen10metaObjectEv(
    const QSplashScreen *self) {
  return self->metaObject();
}

//  QString QSplashScreen::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QSplashScreen2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSplashScreen::tr(s, c, n));
}

//  QSplashScreen::QSplashScreen(const QPixmap &pixmap, Qt::WindowFlags f)
extern "C" Q_DECL_EXPORT
QSplashScreen *ritual_ZN13QSplashScreenC1ERK7QPixmap6QFlagsIN2Qt10WindowTypeEE(
    const QPixmap *pixmap,
    int f) {
  return new QSplashScreen(*pixmap, QFlags<Qt::WindowType>::fromInt(f));
}

//  QSplashScreen::QSplashScreen(QScreen *screen, const QPixmap &pixmap,
//      Qt::WindowFlags f)
extern "C" Q_DECL_EXPORT
QSplashScreen *ritual_ZN13QSplashScreenC1EP7QScreenRK7QPixmap6QFlagsIN2Qt10WindowTypeEE(
    QScreen *screen,
    const QPixmap *pixmap,
    int f) {
  return new QSplashScreen(
      screen,
      *pixmap,
      QFlags<Qt::WindowType>::fromInt(f));
}

//  QSplashScreen::~QSplashScreen()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSplashScreenD1Ev(QSplashScreen *self) {
  delete self;
}

//  void QSplashScreen::setPixmap(const QPixmap &pixmap)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSplashScreen9setPixmapERK7QPixmap(
    QSplashScreen *self,
    const QPixmap *pixmap) {
  self->setPixmap(*pixmap);
}

//  const QPixmap QSplashScreen::pixmap() const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK13QSplashScreen6pixmapEv(const QSplashScreen *self) {
  return new QPixmap(self->pixmap());
}

//  void QSplashScreen::finish(QWidget *w)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSplashScreen6finishEP7QWidget(
    QSplashScreen *self,
    QWidget *w) {
  self->finish(w);
}

//  void QSplashScreen::repaint()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSplashScreen7repaintEv(QSplashScreen *self) {
  self->repaint();
}

//  QString QSplashScreen::message() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QSplashScreen7messageEv(const QSplashScreen *self) {
  return new QString(self->message());
}

//  void QSplashScreen::showMessage(const QString &message, int alignment,
//      const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSplashScreen11showMessageERK7QStringiRK6QColor(
    QSplashScreen *self,
    const QString *message,
    int alignment,
    const QColor *color) {
  self->showMessage(*message, alignment, *color);
}

//  void QSplashScreen::clearMessage()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSplashScreen12clearMessageEv(QSplashScreen *self) {
  self->clearMessage();
}
