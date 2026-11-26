//  Written by hand on 2026-11-25 from
//  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickfocusframe_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator runs
//  again.
//  Qt builds QuickNativeStyle for macOS and Windows only, so the whole
//  file stands under that. Qt does not export the class, so only what
//  its header writes out is called. The default constructor and the
//  destructor are the implicit ones, written as 'new' and 'delete'
//  for Python to make and free it.
//  Not written: the static 'Invalid', which Qt's library does not
//  offer. No file of QtWidgets is included, as 'QStyle' would then
//  be ambiguous in the headers of this part.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_MACOS) || defined(Q_OS_WIN)
#include <QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickfocusframe_p.h>

//  QQuickFocusFrameDescription::QQuickFocusFrameDescription()
extern "C" Q_DECL_EXPORT
QQuickFocusFrameDescription *ritual_ZN27QQuickFocusFrameDescriptionC1Ev() {
  return new QQuickFocusFrameDescription();
}

//  QQuickFocusFrameDescription::~QQuickFocusFrameDescription()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickFocusFrameDescriptionD1Ev(
    QQuickFocusFrameDescription *self) {
  delete self;
}

//  bool QQuickFocusFrameDescription::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QQuickFocusFrameDescription7isValidEv(
    const QQuickFocusFrameDescription *self) {
  return self->isValid();
}

#endif  // defined(Q_OS_MACOS) || defined(Q_OS_WIN)
