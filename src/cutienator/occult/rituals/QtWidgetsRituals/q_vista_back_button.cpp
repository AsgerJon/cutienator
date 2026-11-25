//  Written by hand on 2026-11-25 from
//  QtWidgets/6.12.0/QtWidgets/private/qwizard_win_p.h, Qt 6.12.0, as
//  the Qt of Windows installs it. Kept as it is when the generator
//  runs again. Qt's library offers nothing of this class by name:
//  only its virtual functions are called, through the object, and
//  what its header writes out.
//  Not written: the constructor, which Qt's library offers not.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if defined(Q_OS_WIN) && QT_CONFIG(style_windowsvista) && QT_CONFIG(wizard)
#include <QtWidgets/6.12.0/QtWidgets/private/qwizard_win_p.h>
#include <QtCore/qsize.h>
#include <QtGui/qevent.h>

//  QVistaBackButton::~QVistaBackButton()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QVistaBackButtonD1Ev(QVistaBackButton *self) {
  delete self;
}

//  QSize QVistaBackButton::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK16QVistaBackButton8sizeHintEv(
    const QVistaBackButton *self) {
  return new QSize(self->sizeHint());
}

//  QSize QVistaBackButton::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK16QVistaBackButton15minimumSizeHintEv(
    const QVistaBackButton *self) {
  return new QSize(self->minimumSizeHint());
}

//  void QVistaBackButton::enterEvent(QEnterEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QVistaBackButton10enterEventEP11QEnterEvent(
    QVistaBackButton *self,
    QEnterEvent *event) {
  self->enterEvent(event);
}

//  void QVistaBackButton::leaveEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QVistaBackButton10leaveEventEP6QEvent(
    QVistaBackButton *self,
    QEvent *event) {
  self->leaveEvent(event);
}

//  void QVistaBackButton::paintEvent(QPaintEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QVistaBackButton10paintEventEP11QPaintEvent(
    QVistaBackButton *self,
    QPaintEvent *event) {
  self->paintEvent(event);
}

#endif  // defined(Q_OS_WIN) && QT_CONFIG(style_windowsvista) && QT_CONFIG(wizard)
