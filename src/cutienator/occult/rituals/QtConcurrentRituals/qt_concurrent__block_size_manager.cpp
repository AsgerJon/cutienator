//  Written by dev_tooling.RitualGenerator from the records of
//  QtConcurrent/qtconcurrentiteratekernel.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtConcurrent/qtconcurrent_global.h>
#if !defined(QT_NO_CONCURRENT) || defined(Q_QDOC)
#include <QtConcurrent/qtconcurrentiteratekernel.h>

//  QtConcurrent::BlockSizeManager::BlockSizeManager(QThreadPool *pool, int
//      iterationCount)
extern "C" Q_DECL_EXPORT
QtConcurrent::BlockSizeManager *ritual_ZN12QtConcurrent16BlockSizeManagerC1EP11QThreadPooli(
    QThreadPool *pool,
    int iterationCount) {
  return new QtConcurrent::BlockSizeManager(pool, iterationCount);
}

//  void QtConcurrent::BlockSizeManager::timeBeforeUser()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QtConcurrent16BlockSizeManager14timeBeforeUserEv(
    QtConcurrent::BlockSizeManager *self) {
  self->timeBeforeUser();
}

//  void QtConcurrent::BlockSizeManager::timeAfterUser()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QtConcurrent16BlockSizeManager13timeAfterUserEv(
    QtConcurrent::BlockSizeManager *self) {
  self->timeAfterUser();
}

//  int QtConcurrent::BlockSizeManager::blockSize()
extern "C" Q_DECL_EXPORT
int ritual_ZN12QtConcurrent16BlockSizeManager9blockSizeEv(
    QtConcurrent::BlockSizeManager *self) {
  return self->blockSize();
}

//  bool QtConcurrent::BlockSizeManager::blockSizeMaxed()
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QtConcurrent16BlockSizeManager14blockSizeMaxedEv(
    QtConcurrent::BlockSizeManager *self) {
  return self->blockSizeMaxed();
}

#endif  // !defined(QT_NO_CONCURRENT) || defined(Q_QDOC)
