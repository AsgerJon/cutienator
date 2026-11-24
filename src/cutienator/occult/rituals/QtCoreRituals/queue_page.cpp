//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qthreadpool_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qthreadpool_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QueuePage::QueuePage(QRunnable *runnable, int pri)
extern "C" Q_DECL_EXPORT
QueuePage *ritual_ZN9QueuePageC1EP9QRunnablei(QRunnable *runnable, int pri) {
  return new QueuePage(runnable, pri);
}

//  bool QueuePage::isFull()
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QueuePage6isFullEv(QueuePage *self) {
  return self->isFull();
}

//  bool QueuePage::isFinished()
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QueuePage10isFinishedEv(QueuePage *self) {
  return self->isFinished();
}

//  void QueuePage::push(QRunnable *runnable)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QueuePage4pushEP9QRunnable(
    QueuePage *self,
    QRunnable *runnable) {
  self->push(runnable);
}

//  void QueuePage::skipToNextOrEnd()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QueuePage15skipToNextOrEndEv(QueuePage *self) {
  self->skipToNextOrEnd();
}

//  QRunnable *QueuePage::first()
extern "C" Q_DECL_EXPORT
QRunnable *ritual_ZN9QueuePage5firstEv(QueuePage *self) {
  return self->first();
}

//  QRunnable *QueuePage::pop()
extern "C" Q_DECL_EXPORT
QRunnable *ritual_ZN9QueuePage3popEv(QueuePage *self) {
  return self->pop();
}

//  bool QueuePage::tryTake(QRunnable *runnable)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QueuePage7tryTakeEP9QRunnable(
    QueuePage *self,
    QRunnable *runnable) {
  return self->tryTake(runnable);
}

//  int QueuePage::priority() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QueuePage8priorityEv(const QueuePage *self) {
  return self->priority();
}

//  QueuePage::~QueuePage()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QueuePageD1Ev(QueuePage *self) {
  delete self;
}
