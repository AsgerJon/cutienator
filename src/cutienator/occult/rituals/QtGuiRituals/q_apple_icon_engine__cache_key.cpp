//  Written by hand on 2026-11-25 from
//  QtGui/6.12.0/QtGui/private/qappleiconengine_p.h, Qt 6.12.0, as the Qt of
//  macOS installs it. Kept as it is when the generator runs again.
//  Qt's library offers none of its functions by name, a class inside an
//  exported one being no exported class itself: only what its header
//  writes out is called. Not written: the friend 'qHash'.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if defined(Q_OS_DARWIN)
#include <QtGui/6.12.0/QtGui/private/qappleiconengine_p.h>
#include <QtGui/qpalette.h>
#include <QtCore/qsize.h>

//  QAppleIconEngine::CacheKey::CacheKey(QIcon::Mode mode, QIcon::State
//      state, const QPalette &palette, QSize size, qreal scale)
extern "C" Q_DECL_EXPORT
QAppleIconEngine::CacheKey *ritual_ZN16QAppleIconEngine8CacheKeyC1EN5QIcon4ModeENS1_5StateERK8QPalette5QSized(
    QIcon::Mode mode,
    QIcon::State state,
    const QPalette *palette,
    const QSize *size,
    qreal scale) {
  return new QAppleIconEngine::CacheKey(mode, state, *palette, *size, scale);
}

//  QAppleIconEngine::CacheKey::~CacheKey()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAppleIconEngine8CacheKeyD1Ev(
    QAppleIconEngine::CacheKey *self) {
  delete self;
}

//  bool operator==(const QAppleIconEngine::CacheKey &lhs, const
//      QAppleIconEngine::CacheKey &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKN16QAppleIconEngine8CacheKeyES2_(
    const QAppleIconEngine::CacheKey *lhs,
    const QAppleIconEngine::CacheKey *rhs) {
  return *lhs == *rhs;
}

#endif  // defined(Q_OS_DARWIN)
