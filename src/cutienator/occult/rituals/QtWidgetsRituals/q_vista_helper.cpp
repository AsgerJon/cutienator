//  Written by hand on 2026-11-25 from
//  QtWidgets/6.12.0/QtWidgets/private/qwizard_win_p.h, Qt 6.12.0, as
//  the Qt of Windows installs it. Kept as it is when the generator
//  runs again. Qt's library offers nothing of this class by name:
//  only its virtual functions are called, through the object, and
//  what its header writes out.
//  Not written: the constructor and the functions the header does not
//  write out, which Qt's library offers not, and 'titleBarSize',
//  'titleBarSizeDp', 'frameSize' and 'captionSize', which the header
//  writes out over functions and a number Qt's library offers not.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if defined(Q_OS_WIN) && QT_CONFIG(style_windowsvista) && QT_CONFIG(wizard)
#include <QtWidgets/6.12.0/QtWidgets/private/qwizard_win_p.h>
#include <QtGui/qpaintdevice.h>
#include <QtCore/qcoreevent.h>

//  QVistaHelper::~QVistaHelper()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QVistaHelperD1Ev(QVistaHelper *self) {
  delete self;
}

//  QVistaBackButton *QVistaHelper::backButton() const
extern "C" Q_DECL_EXPORT
QVistaBackButton *ritual_ZNK12QVistaHelper10backButtonEv(
    const QVistaHelper *self) {
  return self->backButton();
}

//  void QVistaHelper::hideBackButton()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QVistaHelper14hideBackButtonEv(QVistaHelper *self) {
  self->hideBackButton();
}

//  int QVistaHelper::topPadding(const QPaintDevice *device)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QVistaHelper10topPaddingEPK12QPaintDevice(
    const QPaintDevice *device) {
  return QVistaHelper::topPadding(device);
}

//  int QVistaHelper::backButtonSize(const QPaintDevice *device)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QVistaHelper14backButtonSizeEPK12QPaintDevice(
    const QPaintDevice *device) {
  return QVistaHelper::backButtonSize(device);
}

//  int QVistaHelper::leftMargin(const QPaintDevice *device)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QVistaHelper10leftMarginEPK12QPaintDevice(
    QVistaHelper *self,
    const QPaintDevice *device) {
  return self->leftMargin(device);
}

//  bool QVistaHelper::eventFilter(QObject *obj, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QVistaHelper11eventFilterEP7QObjectP6QEvent(
    QVistaHelper *self,
    QObject *obj,
    QEvent *event) {
  return self->eventFilter(obj, event);
}

#endif  // defined(Q_OS_WIN) && QT_CONFIG(style_windowsvista) && QT_CONFIG(wizard)
