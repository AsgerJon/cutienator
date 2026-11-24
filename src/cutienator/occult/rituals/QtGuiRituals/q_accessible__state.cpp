//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible_base.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible.h>

//  QAccessible::State::State()
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_ZN11QAccessible5StateC1Ev() {
  return new QAccessible::State();
}

//  bool operator==(const QAccessible::State &first, const QAccessible::State
//      &second)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKN11QAccessible5StateES2_(
    const QAccessible::State *first,
    const QAccessible::State *second) {
  return operator==(*first, *second);
}

//  QAccessible::State::~State()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAccessible5StateD1Ev(QAccessible::State *self) {
  delete self;
}

#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(accessibility)
