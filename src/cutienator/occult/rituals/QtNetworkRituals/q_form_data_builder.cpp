//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qformdatabuilder.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#if (defined(Q_OS_WASM)) || (QT_CONFIG(http))
#if QT_CONFIG(http)
#include <QtNetwork/qformdatabuilder.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qstring.h>
#include <memory>
#include <QtNetwork/QHttpMultiPart>
#include <QtCore/QFlags>
#include <QtNetwork/QFormDataBuilder>

//  QFormDataBuilder::QFormDataBuilder()
extern "C" Q_DECL_EXPORT
QFormDataBuilder *ritual_ZN16QFormDataBuilderC1Ev() {
  return new QFormDataBuilder();
}

//  QFormDataBuilder::QFormDataBuilder(QFormDataBuilder &&other)
extern "C" Q_DECL_EXPORT
QFormDataBuilder *ritual_ZN16QFormDataBuilderC1EOS_(
    QFormDataBuilder *other) {
  return new QFormDataBuilder(std::move(*other));
}

//  QFormDataBuilder &QFormDataBuilder::operator=(QFormDataBuilder &&other)
extern "C" Q_DECL_EXPORT
QFormDataBuilder *ritual_ZN16QFormDataBuilderaSEOS_(
    QFormDataBuilder *self,
    QFormDataBuilder *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QFormDataBuilder::swap(QFormDataBuilder &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QFormDataBuilder4swapERS_(
    QFormDataBuilder *self,
    QFormDataBuilder *other) {
  self->swap(*other);
}

//  QFormDataBuilder::~QFormDataBuilder()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QFormDataBuilderD1Ev(QFormDataBuilder *self) {
  delete self;
}

//  QFormDataPartBuilder QFormDataBuilder::part(QAnyStringView name)
extern "C" Q_DECL_EXPORT
QFormDataPartBuilder *ritual_ZN16QFormDataBuilder4partE14QAnyStringView(
    QFormDataBuilder *self,
    const QString *name) {
  return new QFormDataPartBuilder(self->part(QAnyStringView(*name)));
}

//  std::unique_ptr<QHttpMultiPart> QFormDataBuilder::buildMultiPart(Options
//      options)
extern "C" Q_DECL_EXPORT
std::unique_ptr<QHttpMultiPart> *ritual_ZN16QFormDataBuilder14buildMultiPartE6QFlagsINS_6OptionEE(
    QFormDataBuilder *self,
    int options) {
  return new std::unique_ptr<QHttpMultiPart>(
      self->buildMultiPart(
          QFlags<QFormDataBuilder::Option>::fromInt(options)));
}

//  QFormDataBuilderPrivate *QFormDataBuilder::d_func()
extern "C" Q_DECL_EXPORT
QFormDataBuilderPrivate *ritual_ZN16QFormDataBuilder6d_funcEv(
    QFormDataBuilder *self) {
  return self->d_func();
}

//  const QFormDataBuilderPrivate *QFormDataBuilder::d_func() const
extern "C" Q_DECL_EXPORT
const QFormDataBuilderPrivate *ritual_ZNK16QFormDataBuilder6d_funcEv(
    const QFormDataBuilder *self) {
  return self->d_func();
}

//  a std::unique_ptr<QHttpMultiPart> a ritual of QFormDataBuilder gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QFormDataBuilder__std_unique_ptr_QHttpMultiPart(
    std::unique_ptr<QHttpMultiPart> *self) {
  delete self;
}

#endif  // QT_CONFIG(http)
#endif  // (defined(Q_OS_WASM)) || (QT_CONFIG(http))
