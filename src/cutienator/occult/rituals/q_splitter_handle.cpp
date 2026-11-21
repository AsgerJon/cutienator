//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qsplitter.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qsplitter.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>

//  const QMetaObject *QSplitterHandle::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QSplitterHandle10metaObjectEv(
    const QSplitterHandle *self) {
  return self->metaObject();
}

//  QString QSplitterHandle::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QSplitterHandle2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSplitterHandle::tr(s, c, n));
}

//  QSplitterHandle::QSplitterHandle(Qt::Orientation o, QSplitter *parent)
extern "C" Q_DECL_EXPORT
QSplitterHandle *ritual_ZN15QSplitterHandleC1EN2Qt11OrientationEP9QSplitter(
    Qt::Orientation o,
    QSplitter *parent) {
  return new QSplitterHandle(o, parent);
}

//  QSplitterHandle::~QSplitterHandle()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSplitterHandleD1Ev(QSplitterHandle *self) {
  delete self;
}

//  void QSplitterHandle::setOrientation(Qt::Orientation o)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSplitterHandle14setOrientationEN2Qt11OrientationE(
    QSplitterHandle *self,
    Qt::Orientation o) {
  self->setOrientation(o);
}

//  Qt::Orientation QSplitterHandle::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK15QSplitterHandle11orientationEv(
    const QSplitterHandle *self) {
  return self->orientation();
}

//  bool QSplitterHandle::opaqueResize() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSplitterHandle12opaqueResizeEv(
    const QSplitterHandle *self) {
  return self->opaqueResize();
}

//  QSplitter *QSplitterHandle::splitter() const
extern "C" Q_DECL_EXPORT
QSplitter *ritual_ZNK15QSplitterHandle8splitterEv(
    const QSplitterHandle *self) {
  return self->splitter();
}

//  QSize QSplitterHandle::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK15QSplitterHandle8sizeHintEv(const QSplitterHandle *self) {
  return new QSize(self->sizeHint());
}
