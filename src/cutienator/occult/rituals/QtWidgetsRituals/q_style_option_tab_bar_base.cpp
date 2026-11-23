//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qstyleoption.h>

//  QStyleOptionTabBarBase::QStyleOptionTabBarBase()
extern "C" Q_DECL_EXPORT
QStyleOptionTabBarBase *ritual_ZN22QStyleOptionTabBarBaseC1Ev() {
  return new QStyleOptionTabBarBase();
}

//  QStyleOptionTabBarBase::QStyleOptionTabBarBase(const
//      QStyleOptionTabBarBase &other)
extern "C" Q_DECL_EXPORT
QStyleOptionTabBarBase *ritual_ZN22QStyleOptionTabBarBaseC1ERKS_(
    const QStyleOptionTabBarBase *other) {
  return new QStyleOptionTabBarBase(*other);
}

//  QStyleOptionTabBarBase::QStyleOptionTabBarBase(int version)
extern "C" Q_DECL_EXPORT
QStyleOptionTabBarBase *ritual_ZN22QStyleOptionTabBarBaseC1Ei(int version) {
  return new QStyleOptionTabBarBase(version);
}

//  QStyleOptionTabBarBase::~QStyleOptionTabBarBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QStyleOptionTabBarBaseD1Ev(QStyleOptionTabBarBase *self) {
  delete self;
}
