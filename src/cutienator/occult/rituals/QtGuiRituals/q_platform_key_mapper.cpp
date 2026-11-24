//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformkeymapper.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformkeymapper.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qnamespace.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QPlatformKeyMapper that Python can take functions over in. Every QPlatformKeyMapper
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQPlatformKeyMapperCall0)(const void *, int *);
class CuteQPlatformKeyMapper : public QPlatformKeyMapper {
public:
  using QPlatformKeyMapper::QPlatformKeyMapper;
  CuteQPlatformKeyMapper(const QPlatformKeyMapper &other) : QPlatformKeyMapper(other) {}
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK18QPlatformKeyMapper22queryKeyboardModifiersEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  Qt::KeyboardModifiers QPlatformKeyMapper::queryKeyboardModifiers()
  //      const
  Qt::KeyboardModifiers queryKeyboardModifiers() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformKeyMapperCall0 call = reinterpret_cast<CuteQPlatformKeyMapperCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::KeyboardModifier>::fromInt(given);
    }
    return QPlatformKeyMapper::queryKeyboardModifiers();
  }
};

//  QPlatformKeyMapper::~QPlatformKeyMapper()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlatformKeyMapperD1Ev(QPlatformKeyMapper *self) {
  delete self;
}

//  QList<QKeyCombination> QPlatformKeyMapper::possibleKeyCombinations(const
//      QKeyEvent *event) const
extern "C" Q_DECL_EXPORT
QList<QKeyCombination> *ritual_ZNK18QPlatformKeyMapper23possibleKeyCombinationsEPK9QKeyEvent(
    const QPlatformKeyMapper *self,
    const QKeyEvent *event) {
  return new QList<QKeyCombination>(self->possibleKeyCombinations(event));
}

//  Qt::KeyboardModifiers QPlatformKeyMapper::queryKeyboardModifiers() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QPlatformKeyMapper22queryKeyboardModifiersEv(
    const QPlatformKeyMapper *self) {
  return static_cast<int>(self->queryKeyboardModifiers().toInt());
}

//  a Python function taken by a CuteQPlatformKeyMapper, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformKeyMapper(
    QPlatformKeyMapper *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformKeyMapper *>(self)->take(key, call);
}

//  Qt::KeyboardModifiers QPlatformKeyMapper::queryKeyboardModifiers() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK18QPlatformKeyMapper22queryKeyboardModifiersEv(
    const QPlatformKeyMapper *self) {
  return static_cast<int>(
      self->QPlatformKeyMapper::queryKeyboardModifiers().toInt());
}
