//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcontiguouscache.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcontiguouscache.h>

//  QContiguousCacheData *QContiguousCacheData::allocateData(qsizetype size,
//      qsizetype alignment)
extern "C" Q_DECL_EXPORT
QContiguousCacheData *ritual_ZN20QContiguousCacheData12allocateDataExx(
    qsizetype size,
    qsizetype alignment) {
  return QContiguousCacheData::allocateData(size, alignment);
}

//  void QContiguousCacheData::freeData(QContiguousCacheData *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QContiguousCacheData8freeDataEPS_(
    QContiguousCacheData *data) {
  QContiguousCacheData::freeData(data);
}
