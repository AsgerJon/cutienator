//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qformdatabuilder.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#if (defined(Q_OS_WASM)) || (QT_CONFIG(http))
#if QT_CONFIG(http)
#include <QtNetwork/qformdatabuilder.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qstring.h>

//  QFormDataBuilder::QFormDataBuilder()
extern "C" Q_DECL_EXPORT
QFormDataBuilder *ritual_ZN16QFormDataBuilderC1Ev() {
  return new QFormDataBuilder();
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

#endif  // QT_CONFIG(http)
#endif  // (defined(Q_OS_WASM)) || (QT_CONFIG(http))
