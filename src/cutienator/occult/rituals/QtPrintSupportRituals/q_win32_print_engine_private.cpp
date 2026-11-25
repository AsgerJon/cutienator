//  Written by hand on 2026-11-25 from
//  QtPrintSupport/6.12.0/QtPrintSupport/private/qprintengine_win_p.h, Qt
//  6.12.0, as the Qt of Windows installs it. Kept as it is when the
//  generator runs again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object, and what its
//  header writes out.
//  Not written: the constructor, which needs the destructor Qt's
//  library offers not, and the functions the header does not write
//  out, which it offers not either.
#include <QtPrintSupport/qtprintsupportglobal.h>
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#if defined(Q_OS_WIN) && !defined(QT_NO_PRINTER)
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qprintengine_win_p.h>

//  QWin32PrintEnginePrivate::~QWin32PrintEnginePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QWin32PrintEnginePrivateD1Ev(
    QWin32PrintEnginePrivate *self) {
  delete self;
}

//  QWin32PrintEngine *QWin32PrintEnginePrivate::q_func()
extern "C" Q_DECL_EXPORT
QWin32PrintEngine *ritual_ZN24QWin32PrintEnginePrivate6q_funcEv(
    QWin32PrintEnginePrivate *self) {
  return self->q_func();
}

//  const QWin32PrintEngine *QWin32PrintEnginePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QWin32PrintEngine *ritual_ZNK24QWin32PrintEnginePrivate6q_funcEv(
    const QWin32PrintEnginePrivate *self) {
  return self->q_func();
}

#endif  // defined(Q_OS_WIN) && !defined(QT_NO_PRINTER)
