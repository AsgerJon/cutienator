//  Written by hand on 2026-11-26 from
//  QtGui/6.12.0/QtGui/private/qapplekeymapper_p.h, Qt 6.12.0,
//  from Qt's source. Kept as it is when the generator runs again.
//  Objective-C++: the header declares with AppKit's types, so only a
//  compiler of Objective-C++ on Apple's systems reads it; 'summon' builds
//  this file there only. Qt's library offers the class, and the rituals call
//  it. 'NSEventModifierFlags' is a number, an 'unsigned long'.
#include <QtGui/qtguiglobal.h>
#if defined(Q_OS_MACOS)
#include <QtGui/6.12.0/QtGui/private/qapplekeymapper_p.h>
#include <QtGui/qevent.h>

//  Qt::KeyboardModifiers QAppleKeyMapper::queryKeyboardModifiers() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QAppleKeyMapper22queryKeyboardModifiersEv(
    const QAppleKeyMapper *self) {
  return self->queryKeyboardModifiers().toInt();
}

//  QList<QKeyCombination> QAppleKeyMapper::possibleKeyCombinations(const
//      QKeyEvent *event) const
extern "C" Q_DECL_EXPORT
QList<QKeyCombination> *ritual_ZNK15QAppleKeyMapper23possibleKeyCombinationsEPK9QKeyEvent(
    const QAppleKeyMapper *self,
    const QKeyEvent *event) {
  return new QList<QKeyCombination>(
      self->possibleKeyCombinations(event));
}

//  static Qt::KeyboardModifiers
//      QAppleKeyMapper::fromCocoaModifiers(NSEventModifierFlags
//      cocoaModifiers)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QAppleKeyMapper18fromCocoaModifiersEm(
    unsigned long cocoaModifiers) {
  return QAppleKeyMapper::fromCocoaModifiers(
      NSEventModifierFlags(cocoaModifiers)).toInt();
}

//  static NSEventModifierFlags
//      QAppleKeyMapper::toCocoaModifiers(Qt::KeyboardModifiers a0)
extern "C" Q_DECL_EXPORT
unsigned long ritual_ZN15QAppleKeyMapper16toCocoaModifiersE6QFlagsIN2Qt16KeyboardModifierEE(
    int a0) {
  return QAppleKeyMapper::toCocoaModifiers(
      Qt::KeyboardModifiers::fromInt(a0));
}

//  static QChar QAppleKeyMapper::toCocoaKey(Qt::Key key)
extern "C" Q_DECL_EXPORT
QChar *ritual_ZN15QAppleKeyMapper10toCocoaKeyEN2Qt3KeyE(
    int key) {
  return new QChar(
      QAppleKeyMapper::toCocoaKey(static_cast<Qt::Key>(key)));
}

//  static Qt::Key QAppleKeyMapper::fromCocoaKey(QChar keyCode)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QAppleKeyMapper12fromCocoaKeyE5QChar(
    const QChar *keyCode) {
  return int(QAppleKeyMapper::fromCocoaKey(*keyCode));
}

#endif
