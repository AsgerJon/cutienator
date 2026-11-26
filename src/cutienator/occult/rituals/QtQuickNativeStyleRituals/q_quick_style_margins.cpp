//  Written by hand on 2026-11-25 from
//  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleitem_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator runs
//  again.
//  Qt builds QuickNativeStyle for macOS and Windows only, so the whole
//  file stands under that. Qt does not export the class, so only its
//  inline functions are called. The destructor is the implicit one,
//  written as 'delete self' for Python to free it.
//  Not written: 'operator=', the 'operator<<' to a QDebug, which Qt's
//  library does not offer, and the static meta object of Q_GADGET. No
//  file of QtWidgets is included, as 'QStyle' would then be ambiguous
//  in the headers of this part.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_MACOS) || defined(Q_OS_WIN)
#include <QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleitem_p.h>

//  QQuickStyleMargins::QQuickStyleMargins()
extern "C" Q_DECL_EXPORT
QQuickStyleMargins *ritual_ZN18QQuickStyleMarginsC1Ev() {
  return new QQuickStyleMargins();
}

//  QQuickStyleMargins::QQuickStyleMargins(const QQuickStyleMargins &other)
extern "C" Q_DECL_EXPORT
QQuickStyleMargins *ritual_ZN18QQuickStyleMarginsC1ERKS_(
    const QQuickStyleMargins *other) {
  return new QQuickStyleMargins(*other);
}

//  QQuickStyleMargins::QQuickStyleMargins(const QMargins &margins)
extern "C" Q_DECL_EXPORT
QQuickStyleMargins *ritual_ZN18QQuickStyleMarginsC1ERK8QMargins(
    const QMargins *margins) {
  return new QQuickStyleMargins(*margins);
}

//  QQuickStyleMargins::QQuickStyleMargins(const QRect &outer, const QRect
//      &inner)
extern "C" Q_DECL_EXPORT
QQuickStyleMargins *ritual_ZN18QQuickStyleMarginsC1ERK5QRectS2_(
    const QRect *outer,
    const QRect *inner) {
  return new QQuickStyleMargins(*outer, *inner);
}

//  QQuickStyleMargins::~QQuickStyleMargins()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickStyleMarginsD1Ev(QQuickStyleMargins *self) {
  delete self;
}

//  bool QQuickStyleMargins::operator==(const QQuickStyleMargins &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuickStyleMarginseqERKS_(
    const QQuickStyleMargins *self,
    const QQuickStyleMargins *other) {
  return *self == *other;
}

//  bool QQuickStyleMargins::operator!=(const QQuickStyleMargins &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuickStyleMarginsneERKS_(
    const QQuickStyleMargins *self,
    const QQuickStyleMargins *other) {
  return *self != *other;
}

//  int QQuickStyleMargins::left() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQuickStyleMargins4leftEv(
    const QQuickStyleMargins *self) {
  return self->left();
}

//  int QQuickStyleMargins::right() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQuickStyleMargins5rightEv(
    const QQuickStyleMargins *self) {
  return self->right();
}

//  int QQuickStyleMargins::top() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQuickStyleMargins3topEv(
    const QQuickStyleMargins *self) {
  return self->top();
}

//  int QQuickStyleMargins::bottom() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQuickStyleMargins6bottomEv(
    const QQuickStyleMargins *self) {
  return self->bottom();
}

#endif  // defined(Q_OS_MACOS) || defined(Q_OS_WIN)
