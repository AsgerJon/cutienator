//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qxkbcommon_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the whole file stands under
//  '__has_include(<xkbcommon/xkbcommon.h>)' as well, because Qt's
//  header includes xkbcommon's header, which a machine with Qt's kit
//  but no development headers of xkbcommon lacks. Kept as it is when
//  the generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(xkbcommon) && defined(Q_OS_UNIX) && __has_include(<xkbcommon/xkbcommon.h>)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qxkbcommon_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QString QXkbCommon::lookupStringNoKeysymTransformations(xkb_keysym_t
//      keysym)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QXkbCommon35lookupStringNoKeysymTransformationsEj(
    xkb_keysym_t keysym) {
  return new QString(
      QXkbCommon::lookupStringNoKeysymTransformations(
          keysym));
}

//  int QXkbCommon::keysymToQtKey(xkb_keysym_t keysym, Qt::KeyboardModifiers
//      modifiers)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QXkbCommon13keysymToQtKeyEj6QFlagsIN2Qt16KeyboardModifierEE(
    xkb_keysym_t keysym,
    int modifiers) {
  return QXkbCommon::keysymToQtKey(
      keysym,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers));
}

//  bool QXkbCommon::isLatin1(xkb_keysym_t sym)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QXkbCommon8isLatin1Ej(xkb_keysym_t sym) {
  return QXkbCommon::isLatin1(sym);
}

//  bool QXkbCommon::isKeypad(xkb_keysym_t sym)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QXkbCommon8isKeypadEj(xkb_keysym_t sym) {
  return QXkbCommon::isKeypad(sym);
}

//  QXkbCommon::~QXkbCommon()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QXkbCommonD1Ev(QXkbCommon *self) {
  delete self;
}

#endif  // QT_CONFIG(xkbcommon) && defined(Q_OS_UNIX) && __has_include(<xkbcommon/xkbcommon.h>)
