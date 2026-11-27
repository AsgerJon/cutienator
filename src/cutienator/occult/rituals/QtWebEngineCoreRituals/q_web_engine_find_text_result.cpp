//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/qwebenginefindtextresult.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtWebEngineCore/qwebenginefindtextresult.h>

//  int QWebEngineFindTextResult::numberOfMatches() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QWebEngineFindTextResult15numberOfMatchesEv(
    const QWebEngineFindTextResult *self) {
  return self->numberOfMatches();
}

//  int QWebEngineFindTextResult::activeMatch() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QWebEngineFindTextResult11activeMatchEv(
    const QWebEngineFindTextResult *self) {
  return self->activeMatch();
}

//  QWebEngineFindTextResult::QWebEngineFindTextResult()
extern "C" Q_DECL_EXPORT
QWebEngineFindTextResult *ritual_ZN24QWebEngineFindTextResultC1Ev() {
  return new QWebEngineFindTextResult();
}

//  QWebEngineFindTextResult::QWebEngineFindTextResult(const
//      QWebEngineFindTextResult &other)
extern "C" Q_DECL_EXPORT
QWebEngineFindTextResult *ritual_ZN24QWebEngineFindTextResultC1ERKS_(
    const QWebEngineFindTextResult *other) {
  return new QWebEngineFindTextResult(*other);
}

//  QWebEngineFindTextResult &QWebEngineFindTextResult::operator=(const
//      QWebEngineFindTextResult &other)
extern "C" Q_DECL_EXPORT
QWebEngineFindTextResult *ritual_ZN24QWebEngineFindTextResultaSERKS_(
    QWebEngineFindTextResult *self,
    const QWebEngineFindTextResult *other) {
  return &(self->operator=(*other));
}

//  QWebEngineFindTextResult::~QWebEngineFindTextResult()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QWebEngineFindTextResultD1Ev(
    QWebEngineFindTextResult *self) {
  delete self;
}

//  QWebEngineFindTextResult::QWebEngineFindTextResult(int numberOfMatches,
//      int activeMatch)
extern "C" Q_DECL_EXPORT
QWebEngineFindTextResult *ritual_ZN24QWebEngineFindTextResultC1Eii(
    int numberOfMatches,
    int activeMatch) {
  return new QWebEngineFindTextResult(numberOfMatches, activeMatch);
}
