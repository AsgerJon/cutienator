//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qstatictext_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qstatictext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QStaticTextItem::QStaticTextItem()
extern "C" Q_DECL_EXPORT
QStaticTextItem *ritual_ZN15QStaticTextItemC1Ev() {
  return new QStaticTextItem();
}

//  void QStaticTextItem::setUserData(QStaticTextUserData *newUserData)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QStaticTextItem11setUserDataEP19QStaticTextUserData(
    QStaticTextItem *self,
    QStaticTextUserData *newUserData) {
  self->setUserData(newUserData);
}

//  QStaticTextUserData *QStaticTextItem::userData() const
extern "C" Q_DECL_EXPORT
QStaticTextUserData *ritual_ZNK15QStaticTextItem8userDataEv(
    const QStaticTextItem *self) {
  return self->userData();
}

//  void QStaticTextItem::setFontEngine(QFontEngine *fe)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QStaticTextItem13setFontEngineEP11QFontEngine(
    QStaticTextItem *self,
    QFontEngine *fe) {
  self->setFontEngine(fe);
}

//  QFontEngine *QStaticTextItem::fontEngine() const
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_ZNK15QStaticTextItem10fontEngineEv(
    const QStaticTextItem *self) {
  return self->fontEngine();
}

//  QStaticTextItem::~QStaticTextItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QStaticTextItemD1Ev(QStaticTextItem *self) {
  delete self;
}
