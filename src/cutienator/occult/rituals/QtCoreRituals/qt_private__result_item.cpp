//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qresultstore.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(future)
#include <QtCore/qresultstore.h>

//  QtPrivate::ResultItem::ResultItem()
extern "C" Q_DECL_EXPORT
QtPrivate::ResultItem *ritual_ZN9QtPrivate10ResultItemC1Ev() {
  return new QtPrivate::ResultItem();
}

//  bool QtPrivate::ResultItem::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QtPrivate10ResultItem7isValidEv(
    const QtPrivate::ResultItem *self) {
  return self->isValid();
}

//  bool QtPrivate::ResultItem::isVector() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QtPrivate10ResultItem8isVectorEv(
    const QtPrivate::ResultItem *self) {
  return self->isVector();
}

//  int QtPrivate::ResultItem::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QtPrivate10ResultItem5countEv(
    const QtPrivate::ResultItem *self) {
  return self->count();
}

//  QtPrivate::ResultItem::~ResultItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate10ResultItemD1Ev(QtPrivate::ResultItem *self) {
  delete self;
}

#endif  // QT_CONFIG(future)
