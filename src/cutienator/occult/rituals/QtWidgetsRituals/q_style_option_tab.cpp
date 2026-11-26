//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(tabbar)
#include <QtWidgets/qstyleoption.h>

//  QStyleOptionTab::QStyleOptionTab()
extern "C" Q_DECL_EXPORT
QStyleOptionTab *ritual_ZN15QStyleOptionTabC1Ev() {
  return new QStyleOptionTab();
}

//  QStyleOptionTab::QStyleOptionTab(const QStyleOptionTab &other)
extern "C" Q_DECL_EXPORT
QStyleOptionTab *ritual_ZN15QStyleOptionTabC1ERKS_(
    const QStyleOptionTab *other) {
  return new QStyleOptionTab(*other);
}

//  QStyleOptionTab &QStyleOptionTab::operator=(const QStyleOptionTab &a0)
extern "C" Q_DECL_EXPORT
QStyleOptionTab *ritual_ZN15QStyleOptionTabaSERKS_(
    QStyleOptionTab *self,
    const QStyleOptionTab *a0) {
  return &(self->operator=(*a0));
}

//  QStyleOptionTab::QStyleOptionTab(int version)
extern "C" Q_DECL_EXPORT
QStyleOptionTab *ritual_ZN15QStyleOptionTabC1Ei(int version) {
  return new QStyleOptionTab(version);
}

//  QStyleOptionTab::~QStyleOptionTab()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QStyleOptionTabD1Ev(QStyleOptionTab *self) {
  delete self;
}

#endif  // QT_CONFIG(tabbar)
