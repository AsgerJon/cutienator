//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qlayoutengine_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qlayoutengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QLayoutStruct::init(int stretchFactor, int minSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLayoutStruct4initEii(
    QLayoutStruct *self,
    int stretchFactor,
    int minSize) {
  self->init(stretchFactor, minSize);
}

//  int QLayoutStruct::smartSizeHint()
extern "C" Q_DECL_EXPORT
int ritual_ZN13QLayoutStruct13smartSizeHintEv(QLayoutStruct *self) {
  return self->smartSizeHint();
}

//  int QLayoutStruct::effectiveSpacer(int uniformSpacer) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QLayoutStruct15effectiveSpacerEi(
    const QLayoutStruct *self,
    int uniformSpacer) {
  return self->effectiveSpacer(uniformSpacer);
}

//  QLayoutStruct::~QLayoutStruct()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLayoutStructD1Ev(QLayoutStruct *self) {
  delete self;
}
